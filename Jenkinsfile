pipeline {
   agent { label 'dss-plugin-tests'}
   environment {
        PLUGIN_INTEGRATION_TEST_INSTANCE="/home/jenkins/instance_config.json"
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
             withEnv {
                sh 'echo "Running integration tests"'
                sh 'echo "$HOST"'
                sh """
                   make integration-tests
                   """
                sh 'echo "Done with integration tests"'
             }
         }
      }
   }
   post {
     always {
        junit '*.xml'
        script {
           allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'tests/allure_report']]
            ])
        }
     }
   }
}
