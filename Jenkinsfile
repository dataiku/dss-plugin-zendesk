pipeline {
   agent { label 'dss-plugin-tests'}
   environment {
        HOST = "$dss_target_host"
    }
   stages {
      stage('Install dependencies') {
         steps {
            sh 'echo "Installing deps"'
            sh """
               python3 -m venv venv
               . venv/bin/activate
               pip3 install --upgrade pip3
               pip3 install --no-cache-dir -r tests/python/requirements.txt
            """
            sh 'echo "Done with deps"'
         }
      }
      stage('Run Unit Tests') {
         steps {
            sh 'echo "Running unit tests"'
            sh """
               . venv/bin/activate
               pytest --junitxml=result.xml ./tests/python/unit || true
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
                   pytest --junitxml=result.xml ./tests/python/integration || true
                   """
                sh 'echo "Done with integration tests"'
             }
         }
      }
   }
   post {
     always {
        junit '*.xml'
     }
   }
}
