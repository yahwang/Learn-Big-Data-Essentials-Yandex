### 1. Estimate minimum Namenode RAM size for HDFS with 1 PB capacity, block size 64 MB, average metadata size for each block is 300 B, replication factor is 3. Provide the formula for calculations and the result.

Namenode에 필요한 램 계산
1PB / (64MB * 3) * 300 B = 1.56GB

---

### 2. HDDs in your cluster have the following characteristics: average reading speed is 60 MB/s, seek time is 5 ms. You want to spend 0.5 % time for seeking the block, i.e. seek time should be 200 times less than the time to read the block. Estimate the minimum block size.

최소한의 block size를 계산하라.

Block size: X

최고 Block reading time : 5ms * 200 = 1s

Reading speed : 60 / 1s = X / 1s

X = 60MB

---

### 3. To complete this task use the 'HDFS CLI Playground' item.
Create text file ‘test.txt’ in a local fs. Use HDFS CLI to make the following operations:

•	сreate directory ‘assignment1’ in your home directory in HDFS (you can use a relative path or prescribe it explicitly "/user/jovyan/...")

•	put test.txt in it

•	output the size and the owner of the file

•	revoke ‘read’ permission for ‘other users’

•	read the first 10 lines of the file

•	rename it to ‘test2.txt’.

Provide all the commands to HDFS CLI.

---

hdfs dfs -mkdir /user/jovyan/assignment1 : 하둡에 폴더 생성

hdfs dfs -put ~/test.txt assignment1/test.txt : 로컬파일 하둡으로 복사

hdfs dfs -ls /user/jovyan/assignment1/test.txt : 파일 정보 확인

hdfs dfs -chmod o-r /user/jovyan/assignment1/test.txt : other user의 read 권한 삭제

hdfs dfs -cat /user/jovyan/assignment1/test.txt | head -10 : 앞 10줄 읽기

(head 단독으로는 사용불가하기 때문에 cat과 파이프라인 적용)

hdfs dfs -mv /user/jovyan/assignment1/test.txt /user/jovyan/assignment1/test2.txt : 파일명 변경

---

### 4. To complete this task use the 'HDFS CLI Playground' item.

Use HDFS CLI to investigate the file ‘/data/wiki/en_articles_part/articles-part’ in HDFS:

•	get blocks and their locations in HDFS for this file, show the command without an output

•	get the information about any block of the file, show the command and the block locations from the output

---

hdfs fsck /data/wiki/en_articles_part/articles-part -files -blocks -locations

hdfs fsck /data/wiki/en_articles_part/articles-part

