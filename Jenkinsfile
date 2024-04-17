pipeline {
    agent any
    stages {
        stage('start') {
            agent any
            steps {
                slacksend (channel: '#프로젝트', message: "start")
            }
        }
        
    }
}