from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=320)
    wallet = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.phonenumber}, {self.lastname}, {self.wallet}"

class Game(models.Model):
    game = models.CharField(max_length=30)
    price_per_hour = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.game}, {self.price_per_hour}"
    
    
class Payment(models.Model):
    GAME_CHOICES = (("8", '8 ball'),("PS4", "play staion4"))
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    payment = models.IntegerField()
    use_wallet = models.BooleanField()

    def save(self, *args, **kwargs):
        this_member = Member.objects.get(phonenumber=self.member.phonenumber)
        if self.use_wallet:
            if this_member.wallet >= self.payment:
                this_member.wallet -= self.payment
            else:
                self.payment -= this_member.wallet 
                this_member.wallet = 0
        this_member.wallet += self.payment // 10  # add 10 percent of payment to member wallet as gift
        print(self.payment)
        this_member.save()

        super(Payment, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.member.phonenumber[-4:]}, {self.payment}"