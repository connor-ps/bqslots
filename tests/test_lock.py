#!/usr/bin/env python

"""Tests for `gcs_lock_thing` package."""
import unittest

import bqslots.lock as gcs
from google.cloud import storage


class TestgcsLockThing(unittest.TestCase):
    """Tests for `gcs_lock_thing` package."""
    private_bucket = "data-trf-test-mutex-lock"
    lock_file_name = "test-lock.txt"
    ttl = 2
    client_1 = gcs.Client(bucket=private_bucket, lock_file_path=lock_file_name, expiry=ttl, lock_id_prefix="client_1")
    client_2 = gcs.Client(bucket=private_bucket, lock_file_path=lock_file_name, expiry=ttl, lock_id_prefix="client_2")

    def setUp(self):
        """Set up test fixtures, if any."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(self.private_bucket)
        blobs = bucket.list_blobs(prefix='test-lock.txt')
        for blob in blobs:
            blob.delete()

    def tearDown(self):
        """Tear down test fixtures, if any."""
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(self.private_bucket)
        blobs = bucket.list_blobs(prefix='test-lock.txt')
        for blob in blobs:
            blob.delete()

    def test_basic_lock(self):
        """Test basic use"""
        lock_acquired_status = self.client_1.lock()
        self.assertTrue(lock_acquired_status)
        free_lock_status = self.client_1.free_lock()
        self.assertTrue(free_lock_status)

    def test_lock_not_free(self):
        """
        test lock not free
        """
        lock_acquired_status = self.client_1.lock()
        client_2_lock_acquired_status = self.client_2.lock()
        self.assertTrue(lock_acquired_status)
        self.assertFalse(client_2_lock_acquired_status)

    def test_wait_lock_to_free(self):
        """
        test that lock can be acquired after it has gone stale
        """
        self.client_1.lock()
        client_2_lock_acquired_status = self.client_2.wait_for_lock_expo()
        self.assertTrue(client_2_lock_acquired_status)