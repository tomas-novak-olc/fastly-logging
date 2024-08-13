from tortoise import Model, fields


class LogEntry(Model):
    id = fields.IntField(pk=True, generated=True)
    timestamp = fields.DatetimeField()
    client_ip = fields.CharField(max_length=15)
    geo_country = fields.CharField(max_length=255)
    geo_city = fields.CharField(max_length=255)
    host = fields.CharField(max_length=255)
    url = fields.CharField(max_length=1024)
    request_method = fields.CharField(max_length=10)
    request_protocol = fields.CharField(max_length=10)
    request_referer = fields.CharField(max_length=1024)
    response_state = fields.CharField(max_length=32)
    response_status = fields.CharField(max_length=32)
    response_reason = fields.CharField(max_length=255)
    response_body_size = fields.IntField()
    fastly_server = fields.CharField(max_length=255)
    fastly_is_edge = fields.BooleanField()

    def __str__(self):
        return self.response_status + self.url
