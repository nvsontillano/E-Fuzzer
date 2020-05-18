# E-Fuzzer

## Payloads
The payloads used for the fuzzer were from different github repositories. The url of these repositories are listed in `payload_urls.txt` and `payload_urls.txt`. The folder `payloads_2020-03-02` contains the files downloaded from these repositories.


## Fuzzer
To use the fuzzer, run the `fuzzer/run_scripts.sh` in your terminal. Fill in the required arguments.

`./run_scripts.sh "url" "method" normal_count "cookie" "test_name" "payloads_folder"`

  - url: url of target
  - method: HTTP method to be used for the request
  - normal_count: length of normal HTTP response
  - cookie: cookie to be used in the request
  - test_name: name of web application; this will be used for the directory name
  - payloads_folder: folder where the files containing the payloads


## Result
Each result folder contains a result file of unencoded payloads, result file of encoded payloads and statistics file. The result files only contains the payload that possibly caused a successful sql injection. The statistics contain the number of times an encoding caused a successful sql injection.
