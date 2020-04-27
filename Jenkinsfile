pipeline {
   agent any
   stages {
      stage('Create Bundle') {
         steps {
           sh 'echo "COUCOU"'
           sh 'python --version'
         //   httpRequest authentication: 'dss-creds', httpMode: 'PUT', url: "$host/public/api/projects/$projectKey/bundles/exported/$bundleId"
         //   httpRequest authentication: 'dss-creds', httpMode: 'GET', url: "$host/public/api/projects/$projectKey/bundles/exported/$bundleId/archive", outputFile: 'bundle.zip'
         }
      }
      stage('Upload bundle') {
         steps {
           // httpRequest authentication: 'dss-creds-automation', httpMode: 'POST', url: "$host_automation/public/api/projectsFromBundle/", uploadFile: 'bundle.zip', multipartName: 'file'
           
         }
      }
   }
}
