pipeline {
    agent any
    stages {
        stage('start') {
            agent any
            steps {
                slacksend (channel: '#프로젝트', message: 'start')
            }
        }
        stage('ci') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pylint --ignore-path='tests' $(git ls-files '*.py')
                pytest
                coverage run -m pytest
                coverage report
                coverage html
                '''
            }
        }
        stage('deploy'){
            steps {
                sshagent(credentials:['cicd-pem-username']){
                    sh '''
                    ssh -o "StrictHostKeyChecking no" ec2-user@13.125.97.17 "cd cicd && git pull"
                    '''
                }
            }
        }
        stage('end') {
            steps {
                slacksend(channel: '#프로젝트', message: 'end')
            }
        }        
    }
}