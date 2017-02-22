@Library('fxtest@1.2') _


/** Desired capabilities */
def capabilities = [
  browserName: 'Firefox',
  version: '47.0',
  platform: 'Windows 7'
]

pipeline {
  agent any
  options {
    ansiColor()
    timestamps()
    timeout(time: 1, unit: 'HOURS')
  }
  environment {
    PYTEST_ADDOPTS =
      "-n=10 " +
      "--color=yes " +
      "--tb=short " +
      "--driver=SauceLabs " +
      "--variables=capabilities.json"
    SAUCELABS_API_KEY = credentials('SAUCELABS_API_KEY')
  }
  stages {
    stage('Lint') {
      steps {
        sh "tox -e flake8"
      }
    }
    stage('Test') {
      steps {
        writeCapabilities(capabilities, 'capabilities.json')
        sh "tox -e py27"
      }
      post {
        always {
          archiveArtifacts 'results/*'
          junit 'results/*.xml'
          submitToActiveData('results/py27.log')
          publishHTML(target: [
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: 'results',
            reportFiles: "py27.html",
            reportName: 'HTML Report'])
        }
      }
    }
  }
  post {
    failure {
      mail(
        body: "${BUILD_URL}",
        from: "firefox-test-engineering@mozilla.com",
        replyTo: "firefox-test-engineering@mozilla.com",
        subject: "Build failed in Jenkins: ${JOB_NAME} #${BUILD_NUMBER}",
        to: "fte-ci@mozilla.com")
    }
    changed {
      ircNotification()
    }
  }
}
