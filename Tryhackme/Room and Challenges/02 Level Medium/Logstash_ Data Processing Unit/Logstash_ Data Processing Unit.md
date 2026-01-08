1. No answer needed
2. No answer needed
3. 1. 9200
   2. 8.8.1
   3. systemctl status elasticsearch.service
   4. 192.168.0.1
4. 1. 3s
   2. 8.8.1
5. 1. 5601
   2. 3
   3. No answer needed
6. 1. Mutate
   2. drop
   3. grok
7. 1. nay
   2. path
   3. columns
   4. elasticsearch
8. 1. tcp
   2. csv
9. 1. prune
   2. mutate
   3. rename => { "src_ip" => "source_ip" }
10. 1. yay
    2. stdout
    3. syslog,host,port
11. 1. logstash -f logstash.conf
    2. stdin,csv,stdout
12. No answer needed
