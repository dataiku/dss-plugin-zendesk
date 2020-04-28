pipeline {
   agent any
   stages {
      stage('Create Bundle') {
         steps {
           sh 'echo "COUCOU"'
           sh 'python3 --version'
         //   httpRequest authentication: 'dss-creds', httpMode: 'PUT', url: "$host/public/api/projects/$projectKey/bundles/exported/$bundleId"
         //   httpRequest authentication: 'dss-creds', httpMode: 'GET', url: "$host/public/api/projects/$projectKey/bundles/exported/$bundleId/archive", outputFile: 'bundle.zip'  
        }
      }
      stage('Install dependencies') {
         steps {
            sh 'echo "Installing deps"'
            sh """
               python3 -m venv venv
               . venv/bin/activate
               """
            sh 'echo "Done with deps"'
         }
      }
      stage('Run Unit Tests') {
         steps {
            sh 'echo "Running unit tests"'
            sh """
               . venv/bin/activate
               pytest
               """
            sh 'echo "Done with unit tests"'
         }
      }
   }
}
