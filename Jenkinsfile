pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    // Jenkins Manage Tools me set kiye gaye Scanner ka naam
                    def scannerHome = tool 'SonarQubeScanner'
                    
                    // Jenkins System Configuration me add kiye gaye Server ka naam
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }
    }
}
