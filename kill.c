int sockfd;
int option = 1;
sockfd = socket(AF_INET, SOCK_STREAM, 0);
setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &option, sizeof(option));
