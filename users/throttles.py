from rest_framework import throttling
from utils.functions import request_allowed


class TimeRestrictionThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return request_allowed()


class LoginThrottle(throttling.AnonRateThrottle):
    scope = ""

    def allow_request(self, request, view):
        if request.user and request.user.is_authenticated:
            return True

        # O'zgaruvchilar, xato soni va bloklanish vaqtini saqlash uchun
        self.history = self.get_history(request)
        self.key = self.get_cache_key(request, view)
        self.history.insert(0, self.now)

        print(f"\n\n{self.history}\n{self.key}\n\n")
        # # O'zgaruvchilar, bloklanish o'rtasidagi qanchalik vaqt o'tgani va xatolar sonini saqlash uchun
        # interval = self.timer
        # if len(self.history) > self.num_requests:
        #     if self.now - self.history[-1 - self.num_requests] <= interval:
        #         # 15 daqiqa ichida 3 dan ortiq xatolar yuborsa, 1 soatga bloklaymiz
        #         if self.now - self.history[-1 - self.num_requests] <= 15 * 60:
        #             raise throttling.Throttled(
        #                 message="Bir soat ichida juda ko'p urinishlar jo'natildi.",
        #                 wait=60 * 60,
        #             )

        return True
