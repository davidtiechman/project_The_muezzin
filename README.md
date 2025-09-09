#
PROJECT THE MUEZZIN
#
#
STEP 1
##
The project plan is to receive audio files from some source.
Generate metadata on each file using the pathlib library which includes creation date, file size, full path to the file and file name.
Then publish it to kafka in a topic named references_and_metadata
##
#
STEP 2
#
##
Receive from Kafka what was published in the topic reference_and_metadata in step 2, all the messages with the metadata, and add to each file a unique_id based on the uuid library that is used with a hash on the size and name file fields, and all this so that there is a unique identifier for each database that we insert it into.
After that, we insert the entire file into the MongoDB DB, and to insert the file, we need to convert it to binary format without a library.
After that, we insert all the metadata into the Elasticsearch database so that it is convenient to search for file types.
##
