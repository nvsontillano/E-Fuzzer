#include <curl/curl.h>
#include <stdio.h>
#include <string.h>


int main(int argc, char ** argv[]){



	//printf("%s", argv[1]);

	char buffer[1000];

	fgets(buffer, sizeof(buffer), stdin);

	int length = strlen(buffer);
	buffer[length-1] = '\x00';
	
	CURL *curl = curl_easy_init();
	
	if (curl) {
		char *output = curl_easy_escape(curl, buffer, 0);
		if (output){
			printf("%s", output);
			curl_free(output);
		}
	}

	return 0;	
	
}



