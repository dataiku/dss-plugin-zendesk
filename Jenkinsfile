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
      stage('Preparing env') {
         if (!fileExists('.env')){
               echo 'Creating virtualenv ...'
               sh 'virtualenv --no-site-packages .env'
            }
      }
      stage('Run Unit Tests') {
         steps {
            sh 'echo "Running unit tests"'
            sh """
               . .env/bin/activate
               if [[ -f code-env/python/spec/requirements.txt ]]; then
                  pip install -r code-env/python/spec/requirements.txt
               fi
               pytest
               """
            sh 'echo "Done with unit tests"'
         }
      }
   }
}
