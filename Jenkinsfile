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
               pip3 install -r python-tests/integ/requirements.txt
            """
            sh 'echo "Done with deps"'
         }
      }
      stage('Run Integration Tests') {
         steps {
             withCredentials([string(credentialsId: 'dss-target-admin-api-key', variable: 'API_KEY')]) {
                sh 'echo "Running integration tests"'
                sh 'echo "$HOST"'
                sh """
                   . venv/bin/activate
                   pytest --junitxml=result.xml ./python-tests/integ || true
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
