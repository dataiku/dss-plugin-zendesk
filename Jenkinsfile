pipeline {
   options { disableConcurrentBuilds() }
   agent { label 'dss-plugin-tests'}
   environment {
        PLUGIN_INTEGRATION_TEST_INSTANCE="/home/jenkins-agent/instance_config.json"
        SLACK_HOOK=credentials("slack_hook")
    }
   stages {
      stage('Run Unit Tests') {
         steps {
            sh 'echo "Running unit tests"'
            catchError(stageResult: 'FAILURE') {
            sh """
               make unit-tests
               """
            }
            sh 'echo "Done with unit tests"'
         }
      }
      stage('Run Integration Tests') {
         steps {
            sh 'echo "Running integration tests"'
            catchError(stageResult: 'FAILURE') {
            sh """
               make integration-tests
               """
            }
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
            
            sh "file_name=\$(echo ${env.JOB_NAME} | tr '/' '-').status; touch \$file_name; echo \"${env.BUILD_URL},${env.CHANGE_TITLE},${status}\" >> /home/jenkins-agent/daily-statuses/\$file_name"
            
            def subject = "*Plugin* : ${env.JOB_NAME}"
            def job_info = "*Build number* : ${env.BUILD_NUMBER}"
            def status_info = "*Status* : ${status}"
            def build_url = "*Build* : ${env.BUILD_URL}"
            def allure_report = "*Report* : ${env.BUILD_URL}/allure"
            def summary = "${subject}\n${status_info}\n\n${job_info}\n${build_url}\n${allure_report}"

            
            if (status == 'UNSTABLE')
            {
               colorCode = '#FFC300'
               slackSend(color: colorCode, message: summary, notifyCommitters: true)
            }
            if (status == 'FAILURE')
            {
               slackSend(color: colorCode, message: summary, notifyCommitters: true)
            }
            
        }
         
     }
   }
}
