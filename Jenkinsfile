#!/usr/bin/env groovy

def branch = env.BRANCH_NAME ?: 'master'

/** Desired capabilities */
def capabilities = [
  browserName: 'Firefox',
  version: '66.0',
  platform: 'Windows 10'
]

pipeline {
  agent any
  libraries {
    lib('fxtest@1.10')
  }
  triggers {
    pollSCM(branch == 'master' ? 'H/5 * * * *' : '')
    cron(branch == 'master' ? 'H H * * *' : '')
  }
  options {
    ansiColor('xterm')
    timestamps()
    timeout(time: 1, unit: 'HOURS')
  }
  environment {
    PYTEST_PROCESSES = "${PYTEST_PROCESSES ?: "auto"}"
    PYTEST_ADDOPTS =
      "-n=${PYTEST_PROCESSES} " +
      "--tb=short " +
      "--color=yes " +
      "--driver=SauceLabs " +
      "--variables=capabilities.json"
    PULSE = credentials('PULSE')
    SAUCELABS = credentials('SAUCELABS')
  }
  stages {
    stage('Lint') {
      agent {
        dockerfile true
      }
      steps {
        sh "tox -e flake8"
      }
    }
    stage('Test') {
      parallel {
        stage('py36') {
          agent {
            dockerfile true
          }
          steps {
            writeCapabilities(capabilities, 'capabilities.json')
            sh "tox -e py36"
          }
          post {
            always {
              stash includes: 'results/py36.html', name: 'py36'
              archiveArtifacts 'results/*'
              junit 'results/*.xml'
            }
          }
        }
        stage('py27') {
          agent {
            dockerfile true
          }
          steps {
            writeCapabilities(capabilities, 'capabilities.json')
            sh "tox -e py27"
          }
          post {
            always {
              stash includes: 'results/py27.html', name: 'py27'
              archiveArtifacts 'results/*'
              junit 'results/*.xml'
              submitToActiveData('results/py27_raw.txt')
              submitToTreeherder('fxapom', 'T', 'Tests', 'results/*', 'results/py27_tbpl.txt')
            }
          }
        }
      }
    }
  }
  post {
    always {
      unstash 'py36'
      unstash 'py27'
      publishHTML(target: [
        allowMissing: false,
        alwaysLinkToLastBuild: true,
        keepAll: true,
        reportDir: 'results',
        reportFiles: "py36.html, py27.html",
        reportName: 'HTML Report'])
    }
    changed {
      ircNotification()
    }
    failure {
      emailext(
        attachLog: true,
        attachmentsPattern: 'results/*.html',
        body: '$BUILD_URL\n\n$FAILED_TESTS',
        replyTo: '$DEFAULT_REPLYTO',
        subject: '$DEFAULT_SUBJECT',
        to: '$DEFAULT_RECIPIENTS')
    }
  }
}
