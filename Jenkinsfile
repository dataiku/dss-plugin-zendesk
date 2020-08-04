pipeline {
   agent { label 'dss-plugin-tests'}
   environment {
        HOST = "$dss_target_host"
    }
   stages {
/*       stage('Install dependencies') {
         steps {
            sh 'echo "Installing deps"'
            sh """
            """
            sh 'echo "Done with deps"'
         }
      } */
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
             withCredentials([string(credentialsId: 'dss-target-admin-api-key', variable: 'API_KEY')]) {
                sh 'echo "Running integration tests"'
                sh 'echo "$HOST"'
                sh """
                   . venv/bin/activate
                   pytest --junitxml=integration.xml ./tests/python/integration || true
                   """
                sh 'echo "Done with integration tests"'
             }
         }
      }
   }
   post {
     always {
        junit 'unit.xml integration.xml'
     }
   }
}
