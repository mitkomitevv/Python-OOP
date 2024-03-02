class EmailValidator:

    def __init__(self, min__length, mails, domains):
        self.min_length = min__length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail):
        return mail in self.mails

    def __is_domain_valid(self, domain):
        return domain in self.domains

    def validate(self, email):
        username, info = email.split("@")
        mail, domain = info.split(".")

        return self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)
