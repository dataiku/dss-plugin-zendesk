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
            if (status == 'SUCCESS')
            {
               colorCode = '#FF0000'
            }
            if (status == 'UNSTABLE')
            {
               colorCode = '#FFC300'
            }
            
            def subject = "Plugin : ${env.JOB_NAME}"
            def job_info = "Build number : ${env.BUILD_NUMBER}"
            def status_info = "Status : ${status}"
            def build_url = "Build : ${env.BUILD_URL}"
            def allure_report = "Report : ${env.BUILD_URL}/allure"
            def summary = "${subject} ${job_info} ${status_info} ${build_url} ${allure_report} ${summary}"
            def slackResponse = slackSend(color: colorCode, message: summary, notifyCommitters: true)
            slackSend(channel:slackResponse.threadId, message: a thread message)

        }
         
     }
   }
}
