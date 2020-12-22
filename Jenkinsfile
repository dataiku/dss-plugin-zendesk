pipeline {
   options { disableConcurrentBuilds() }
   agent { label 'dss-plugin-tests'}
   environment {
        PLUGIN_INTEGRATION_TEST_INSTANCE="/home/jenkins-agent/instance_config.json"
    }
   stages {
      stage('Run Unit Tests') {
         steps {
            sh 'echo "Running unit tests"'
            sh """
               make unit-tests
               """
            sh 'echo "Done with unit tests"'
         }
      }
      stage('Run Integration Tests') {
         steps {
            sh 'echo "Running integration tests"'
            sh 'echo "$HOST"'
            sh """
               make integration-tests
               """
            sh 'echo "Done with integration tests"'
         }
      }
   }
   post {
     always {
        script {
            allure([
                     includeProperties: false,
                     jdk: '',
                     properties: [],
                     reportBuildPolicy: 'ALWAYS',
                     results: [[path: 'tests/allure_report']]
            ])
            def colorCode = '#FF0000'
            def status = currentBuild.currentResult
            if (currentBuild.currentResult == 'SUCCESS')
            {
               colorCode = '#FF0000'
            }
            if (currentBuild.currentResult == 'UNSTABLE')
            {
               colorCode = '#FFC300'
            }

            blocks= [
            [
            "type": "header",
            "text": {
            "type": "plain_text",
            "text": "Plugin Job : ${env.JOB_NAME} ",
            "emoji": true
            ]
            ],
            [
            "type": "divider"
            ],
            [
            "type": "section",
            "text": [
            "type": "mrkdwn",
            "text": "Run information : ${env.BUILD_URL}"
            ]
            ],
            [
            "type": "section",
            "text": ]
            "type": "mrkdwn",
            "text": "Allure report : ${env.BUILD_URL}"
            [
            ]
            ]
            
            def subject = "${status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"
            def summary = "${subject} (${env.BUILD_URL})"
            slackSend(color: colorCode, blocks: blocks)
        }
         
     }
   }
}
