class Bucket:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Bucket(0)
        self.tail = Bucket(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.nodes = {}

    def insert_after(self, prev, node):
        node.prev = prev
        node.next = prev.next

        prev.next.prev = node
        prev.next = node

    def remove_bucket(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev

    def inc(self, key):

        if key not in self.nodes:

            if self.head.next == self.tail or self.head.next.count > 1:
                bucket = Bucket(1)
                self.insert_after(self.head, bucket)
            else:
                bucket = self.head.next

            bucket.keys.add(key)
            self.nodes[key] = bucket
            return

        cur = self.nodes[key]
        nxt = cur.next

        if nxt == self.tail or nxt.count != cur.count + 1:
            new_bucket = Bucket(cur.count + 1)
            self.insert_after(cur, new_bucket)
        else:
            new_bucket = nxt

        new_bucket.keys.add(key)
        self.nodes[key] = new_bucket

        cur.keys.remove(key)

        if not cur.keys:
            self.remove_bucket(cur)

    def dec(self, key):

        cur = self.nodes[key]

        if cur.count == 1:

            del self.nodes[key]
            cur.keys.remove(key)

            if not cur.keys:
                self.remove_bucket(cur)

            return

        prev = cur.prev

        if prev == self.head or prev.count != cur.count - 1:
            new_bucket = Bucket(cur.count - 1)
            self.insert_after(prev, new_bucket)
        else:
            new_bucket = prev

        new_bucket.keys.add(key)
        self.nodes[key] = new_bucket

        cur.keys.remove(key)

        if not cur.keys:
            self.remove_bucket(cur)

    def getMaxKey(self):

        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys))

    def getMinKey(self):

        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys))