pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', credentialsId: 'be931eed-297a-4c57-9706-565d76161ee0', url: 'https://github.com/WitesoAI/Sentigram'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                    chmod +x Sentigram/envsetup.sh
                    ./Sentigram/envsetup.sh
                    '''
                }
            }
        }

        stage('Configure Ngnix') {
            steps {
                script {
                    sh 'sudo cp -rf DevOps/sentigram.conf /etc/nginx/sites-available/sentigram'
                    try {
                        sh 'sudo rm /etc/nginx/sites-enabled/sentigram'
                    } catch (Exception e) {
                        echo "Nginx Config does'nt exist: ${e.message}"
                    }
                    sh 'sudo ln -s /etc/nginx/sites-available/sentigram /etc/nginx/sites-enabled'
                    sh 'sudo nginx -t'
                    sh 'sudo systemctl reload nginx'
                }
            }
        }

        stage('Stop Gunicorn') {
            steps {
                script {
                    try {
                        sh 'sudo systemctl stop gunicorn_django.socket gunicorn_django.service'
                    } catch (Exception e) {
                        echo "Gunicorn service does'nt exist: ${e.message}"
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    sh 'sudo cp -rf DevOps/gunicorn_sentigram.socket /etc/systemd/system/'
                    sh 'sudo cp -rf DevOps/gunicorn_sentigram.service /etc/systemd/system/'
                    sh 'sudo systemctl daemon-reload'

                    sh 'sudo systemctl start gunicorn_sentigram.socket'
                    sh 'echo "Gunicorn Django Socket has started."'

                    sh 'sudo systemctl enable gunicorn_sentigram.socket'
                    sh 'echo "Gunicorn Django Socket has been enabled."'

                    sh 'sudo systemctl status gunicorn_sentigram.socket'

                    sh 'sudo systemctl start gunicorn_sentigram'
                    sh 'echo "Gunicorn Django has started."'

                    sh 'sudo systemctl enable gunicorn_sentigram'
                    sh 'echo "Gunicorn Django has been enabled."'

                    sh 'sudo systemctl status gunicorn_sentigram'
                    sh 'sudo systemctl restart gunicorn_sentigram'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
    }
}