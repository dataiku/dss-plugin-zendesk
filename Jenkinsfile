pipeline {
   agent any
   stages {
      stage('Install dependencies') {
         steps {
            sh 'echo "Installing deps"'
            sh """
               echo "
            pandas==0.23.4
            python-dateutil==2.8.0
            pytz==2019.2
            requests==2.22.0

            decorator==4.4.0
            ipykernel==4.8.2
            ipython_genutils==0.2.0
            jupyter_client==5.2.4
            jupyter_core==4.4.0
            pexpect==4.7.0
            pickleshare==0.7.5
            ptyprocess==0.6.0
            pyzmq==18.0.2
            simplegeneric==0.8.1
            tornado==5.1.1
            traitlets==4.3.2" > requirements.txt
            """
            sh "cat code-env/python/spec/requirements.txt >> requirements.txt"
            sh """
               python3 -m venv venv
               . venv/bin/activate
               pip3 install -r requirements.txt
            """
            sh 'echo "Done with deps"'
         }
      }
      stage('Run Unit Tests') {
         steps {
            sh 'echo "Running unit tests"'
            sh """
               . venv/bin/activate
               pytest --junitxml=result.xml
               """
            sh 'echo "Done with unit tests"'
         }
      }
   }
   post {
     always {
        junit '*.xml'
     }
   }
}
