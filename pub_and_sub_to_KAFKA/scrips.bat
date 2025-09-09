# זה לא עובד לי
kafka-topics.sh --bootstrap-server localhost:9092 --list
# זה עובד
docker exec -t kafka /usr/bin/kafka-topics --bootstrap-server localhost:9092 --list


kafka-console-consumer --bootstrap-server localhost --topic references_and_metadata --from-beginning
