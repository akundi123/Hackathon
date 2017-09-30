from marketing_notifications_python.models import app_db


def send_message(self, to, message, image_url):
    self.twilio_client.messages.create(
        to = to,
        from_ = phone_number(),
        body = message,
        media_url = image_url
    )
    @views.route('/', methods=['GET', 'POST'])
    @views.route('notifications', methods=['GET', 'POST'])
    def notifications():
        form = SendMessageForm()
        if request.method == 'POST' and form.validate_on_submit():

