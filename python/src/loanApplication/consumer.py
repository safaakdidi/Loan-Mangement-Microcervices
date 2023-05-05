import pika,sys,os,time
from pymongo import MongoClient
import gridfs
from convert import to_mp3


def main():
    client=MongoClient("host.minikube.internal",27017)
    db_docs=client.documents
    db_content=client.content
    #gridfs
    fs_docs=gridfs.GridFS(db_docs)
    fs_content=gridfs.GridFs(db_content)

    #rabbitmq connection

    conn=pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )
    channel=conn.channel()
    def callback(ch,method,properties,body):
        err=to_mp3.start(body,fs_docs,fs_content,ch)
        if err:
            ch.basic_nack(delivery_tag=method.delivery_tag)
        else:
            ch.basic_ack(delivery_tag=method.delivery_tag)
    channel.basic_consume(
        queue=os.environ.get("DOCUMENT_QUEUE"),on_message_callback=callback
    )

    print("Waiting for messages.To exit press CTRL+C")
    channel.start_consuming()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)