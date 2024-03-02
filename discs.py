class Disc:
    total = 0
    company_list = []
    all_discs = []
    #potential future implementation for not having to put in the flight numbers if the same disc is already in database
    #flight_numbers = []
    TYPES = {
    15:'distance driver',
    10:'fairway driver',
    6:"mid range",
    4:'putter'}

    def __init__(self, company, name, speed, glide, turn, fade, color):
        self.speed = speed
        self.glide = glide
        self.turn = turn
        self.fade = fade
        self.company = company.lower()
        self.color = color
        self.name = name
        Disc.total += 1
        Disc.new_company(self.company)
        global all_discs
        Disc.all_discs.append(self)

    #Determines what type of disc it is  
    @property
    def _type(self):
        for i in Disc.TYPES:
            if self.speed <= i:
                disc_type = Disc.TYPES[i]
            else:
                break
        return disc_type
    #for future implementation
    # @property
    # def count(self):
    #     return (Disc.disc_counts.get(self.name, 0))
    
    @property
    def flight_nums(self):
        return (f'{self.speed},{self.glide},{self.turn},{self.fade}')

    @classmethod
    def new_company(cls, company):
        if company not in Disc.company_list:
            Disc.company_list.append(company)

    @classmethod
    def remove_disc(cls, disc):
        cls.all_discs.remove(disc)
        cls.total -= 1