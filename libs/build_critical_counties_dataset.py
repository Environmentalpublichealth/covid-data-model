#!/usr/bin/env python
from io import BytesIO
import boto3
import os

class DatasetDeployer():
    def __init__(self, key='filename.csv', body='a random data', output_dir='.'):
        self.s3 = boto3.client('s3')
        # Supplied by ENV on AWS
        # BUCKET_NAME format is s3://{BUCKET_NAME}
        self.bucket_name = os.environ.get('BUCKET_NAME')
        self.key = key
        self.body = body
        self.output_dir = output_dir

    def _persist_to_s3(self):
        """Persists specific data onto an s3 bucket.
        This method assumes versioned is handled on the bucket itself.
        """
        print('persisting {} to s3'.format(self.key))

        response = self.s3.put_object(Bucket=self.bucket_name,
                                      Key=self.key,
                                      Body=self.body,
                                      ACL='public-read')
        return response

    def _persist_to_local(self):
        """Persists specific data onto an s3 bucket.
        This method assumes versioned is handled on the bucket itself.
        """
        print('persisting {} to local'.format(self.key))

        with open(os.path.join(self.output_dir, self.key), 'wb') as f:
            # hack to allow the local writer to take either bytes or a string
            # note this assumes that all strings are given in utf-8 and not,
            # like, ASCII
            f.write(self.body.encode('UTF-8') if isinstance(self.body, str) else self.body)

        pass

    def persist(self):
        if self.bucket_name:
            self._persist_to_s3()
        else:
            self._persist_to_local()
        return
