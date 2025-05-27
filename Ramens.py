#Diego Osornio
#3/11/2025
import random

ramentypes = ["XXLBihunSegeraPenangWhiteCurry","MiInstanMiKeritingGorengSpesial","OrientalKitchenDriedInstantNoodlesTruffleFlavour","JinJjajangSmokedBlackBeanFlavor","SamyandRamen","XXLBihunSegeraSupAyam","CupStarBatmanGarlicShrimpAji","CornBihunHot&SpicyFriedBihun","3FlavorsIn1Noodleâ€“RiceNoodle","CupTaiwanRamen","SeafoodJjamppongRamyeon","MenShokuninKoidashiNiboshiShoyu","UFOPokkmyeonKoiKoiKankokuFuAmakaraCarbo","WontonMenDonburiButamanChukaSoba","Hot&SourPorkBoneRamen","SurfmamaGooseOilZhajiangNoodle","BudaeRamyun","ShiromaruClassicRamen","MeteorNoodlesWithHot&SourSauce","JiwaPagiMiInstanAyamBawang","3FlavorsIn1Noodleâ€“Guanmiao","LocabodeliCocoIchibanyaKanshuCurryRamenToushitsuOff","BowlNoodlesSavoryChickenFlavor","CornBihunOriginalFriedBihun","LargeSauceYakisoba","TangleBulgogiAlfredoTangluccine","BuldakBasil&CreamUdon","VegetarianNoodles","CupNoodlesCreamyTomYamFlavour","RamenNoodleSoupBirriaFlavor","MenudoInstantRamenNoodle","Mr.NoodlesInstantNoodlesCurryFlavour","ItsumonoIppaiWantanmenShoyuTonkotsu","NarutoShippudenIchirakuRamenCandy","ChickenRamenDonburi","Hot&SourFlavorKonjacNoodle","PozoleFlavorInstantRamenNoodle","AkamaruModernRamen","KelpSeasonalVegetableFlavorPumpkinKonjacNoodle","BuldakHotChickenStir-friedNoodlesJjajang","Garlic&VegetableInstantRiceNoodleSoup","OishiNaniwanoUshioRamenShoyu","UdonNoodlesWithSeafoodFlavor","MiGorengRasaAyamPop","MeteorNoodlesWithBraisedBeefSauce","SrirachaShrimpRamenNoodleSoupMealKit","ChiliPanMee","CupNoodlesTomYamSeafoodFlavour","GhostPepperCheeseSpicyChickenFlavour","HypeAbisMiKuahRasaSeblakHotJeletot","PremiumBraisedBeefNoodleSoup","JiwaPagiMiInstanMieGoreng","GummyNoodlesSoftCandyMix","RasaAyam","SesameClearSoupNoodles","MieGorengRasaSambalTerasi","noAssariOdashigaOishiiDonbeiKizamiAgeUdon","GreenTomYumSoupNoodles","JiwaPagiMiInstanRasaSotoSegeer","KuzeFukuMainichiYasaiDashiShioRamen","HabaneroKimchiJjigaeFlavour","TategataNomihosuNiigataNagaokaShogaShoyuRamen","MiInstanRasaKalduAyam","GhostPepperSpicyChickenFlavourDryBlackInstantNoodles","PremiumGooseOilWithCrispyShallotFlakes","MaruumaTonkotsuRamen","U.F.O.KoikoiTarakoYakisoba","MiGorengRasaCabeIjo","PokÃ©monNoodlesShoyuRamen","HypeAbisMiGorengRasaAyamGeprek","Ganbare!JukenseiMenzukuriKatsuobushiKaoruGyokaiShoyu","BulgogiHotPotFlavourNoodle","MiBonCabeRasaMieGorengLevel15Spicy","Ganbare!JukenseiHotWontonKatsuobushiKaoruTamagoSoup","KimchiRamyeon","ShinRamyunBokkeummyeon","YokohamaIekeiTonkotsuRamen","HabaneroSpicyChickenFlavour","MiGorengPerisaRendangLegenda","PremiumBlackSesameOilWithMashedGinger","HyobanyaLayeredKakitamaSpicySaltRamen","SpicyMushroomRamyeon","KumamotoTonkotsuRamen","GhostPepperSpicyChickenFlavour","BIGCupNoodlesTomYamSeafoodFlavour","JiaxuStirredNoodles","SpicySakuraPrawnSoup","AgedShaoxingWineWithChickenDrumstickSoupNoodle","PokÃ©monNoodlesTomatoCreamFlavor","GhostPepperCheeseSpicyChickenFlavour","TomatoTonkotsu","KitakataLightSoySauceFlavor","MiGorengPerisaRendangLegenda","BIGCupNoodlesJapaneseCheeseCurry","HaeBeeHiamNon-FriedRiceVermicelli","PenangFavouriteHokkienPrawnNoodle","BIGCupNoodlesSeafoodFlavour","DonbeiKitsuneUdonKimetsunoYaiba","BowlNoodlesSpicyKimchiFlavor","BIGCupNoodlesSpicyTonkotsuFlavour","PremiumGonghwachunInstantNoodleWithBlackBeanSauce","TomYumGoong","NostalgicBurntSoySauceRamen","WakameRamenwithMieIseShrimpandSoySauceDashi","RabokkiFlavour","PokÃ©monNoodleOnionConsommÃ©Flavor","PremiumGooseOilWithSichuanPepper&HotChili","KumamotoSpicyTonkotsuRamen","GyoranteiKansyuuYokosukaKaigunCurryUdon","ScienceNoodle(HotPotversion)","PerisaLontong","SeaweedFlavourSoupNoodle","CupNoodleGyozaBig","PerisaLaksaKari","Seafood&VegetableMisoDashiRamen","PepperCrispyPorkNoodles","KakeRamenDesseShoyu","JinJjambbongSpicySeafoodNoodle","GoldSoySauceFlavorCraftRamenNoodles","LanZhouLaMian","TonkotsuRamen","DemaeRamenSeafoodFlavor","MalatangUdon","JapaneseStyleBBQPorkTonkotsuRamen","noAssariOdashigaOishiiDonbeiAgedamaSoba","TopRamenSoySauceFlavorRamenNoodleSoup","MaruumaWantanChukaSoba","MenzukuriYuzu&KoshoKaoruToripaitan","CupStarBBQChickenFlavor","ChowMeinTeriyakiBeefFlavorChowMeinNoodles","AjiyokataiTonkotsuRamenHakata","DashinoUmamideGennennToritakiUdon","YakisobaTeiryakiBeefFlavorJapaneseHomeStyleNoodles","noDonbeiOntsuyuOsoumenMini","LateNightRiceNoodles","CharumeraDonburiTokyoKaidashiChukaSoba","BowlNoodlesRamenNoodlesWithSeasoningMixHot&SpicyFlavor","BihunJagungCornVermicelli","SpicyCoconut&RiceNoodles","SoupHarusameHakataMizutakifuYuzuKosho","CharumeraCupMiso","GummyNoodles","PokÃ©monNoodleCornButterShoyu","PenangBlackCurryNoodle","MandarinStyleNoodleWithOriginalSoySauce40%ReducedSodium","GOLDSpicyMisoRamen","NoodleKitWithSauceTeriyakiSesame","OriginalxCiptarasaMiGoreng","PancitCantonToyomansiFlavor","Mr.NoodlesInstantNoodlesSpicyTomatoFlavour","MiojoLamenDoceSaborBeijinho","TategataNomihosuIppaiSapporoEbiMisoRamen","MiojoTurmaDoChicoBentoSaborCaldinhoDeFeijao","JinRamenVeggie","PremiumxNissinStarSouplessTantanmen","NoodleDoodleFieryCatpata","SumatanxWantanmenDonburiEbishioAji","MiliOneHuongViSuon","MiojoTurmaDaMonicaSaborGalinhaSuave","NoodleHarusame1/3NichibunChanponAji","RoastedSoySauceChickenv3.0","FlatxCipratasaRasaAyamBawang","xTRYToyboxShoyuRamen","AssariOishiiCupNoodleCurry","TategataMiyazakiKaramen","SoupHarusameWantan","KanzenMealAburaSoba","BuldakYakisobaHOTChickenFlavorRamen","SignatureDryNoodle","ChineseSesameOilLionâ€™sManeMushroomPumpkinKonjacNoodle","RamenSpicyTantanmen","BuldakStewTypeRamenSoup","MiTrungKhongChien","LoMeinDanDanNoodleSpicyTeriyaki","InstantPancitCantonChilimansiFlavor","RosÃ©BuldakStir-friedNoodles","U.F.O.SingaporeBlackPepperCrabFlavour","MiojoTurmaDaMonicaSaborTomateSuave","MiHuongViLauThaiTom","U.F.O.KoreanHotChickenFlavour","Praja!LamenSaborCarne","Mr.NoodlesInstantNoodlesBeefFlavour","BeefPhov3.0","BuldakCreamCarbonaraArtificialHotChickenFlavorRamen","RamenNoodleSoupCreamyChickenFlavor","MukashiNagaranoChahanAjiYakisoba","BuldakCarbonaraArtificialSpicyChickenFlavorRamen","VeganWhiiteMisov3.0","Gold/MyojoMyojoTomitaTonkotsuRamen","GarlicPorkTonkotsuv3.0","Koize!Ippei-chanKaraageSyoyuRamen","BuldakQuattroCheeseArtificialSpicyChickenFlavorRamen","Teus-saeRamen","VeganJapaneseCurryv3.0","ChickenRamenShirunashiDonburiJunkissanoNapolitan","Gold/MaruchanIidaShotenRamen","MassamanCurryv3.0","RamenYokozunaTonkotsuShoyu","BuldalJjamppong","YuzuShoyuv3.0","HiyashiChukaMazesoba","Ippei-chanYakisoba","VeganSichuanChiliEditionv3.0","U.F.O.OsakaTakoyakiFlavourYakisoba","BT21DanDanNoodleDreamTeamScallionSauce","RamenNoodleSoup45thAnniversaryChickenFlavor","SrirachaRamenNoodleSoupOriginal"]
ratings = ["5","5","4.5","4.5","5","3.75","3.75","5","5","3.5","3.75","2.5","3.75","3.5","4.25","5","5","5","5","2.5","5","4","4","4","2.5","5","4.5","5","5","4.5","3.75","3.25","4.5","4","5","4.5","5","5","5","1.5","4","3.5","4","5","5","4","5","5","4","2.5","5","3.25","3.5","5","4.5","5","3.5","5","3.75","5","3.5","3.75","3.75","3.75","5","4","2","4.5","3.75","5","3.75","3.5","4.5","3.75","5","5","3.5","3.75","5","5","2","4.5","4","4.5","5","5","5","1.5","4","5","4","5","1","5","5","2","4.5","5","5","5","3","1.75","4","3.5","5","5","4.25","3.5","5","4","4","5","2","5","3.5","5","4.25","435","3","3.5","3.75","5","3.75","4","2","4","2","3.75","3.5","4","2.5","3.5","2.5","3.5","5","5","2","2.75","3.5","0","3.5","5","5","5","0.25","5","5","3.25","3.75","3","3.5","4.5","5","3.75","3.25","3.5","3.75","5","5","5","5","3.75","3.25","5","5","5","5","5","5","3.75","5","3.5","5","5","4","3.5","3.75","0","3","1","3.5","5","5","2.25","5","3.5","3.5","3.75","4.5","5","4","4.5","0","5","5","5","3.75","4.75","5","5","5","4.25","3","3.5","3.75"]
country = ["Malaysia","Indonesia","Thailand","UnitedStates","UnitedStates","Malaysia","Japan","Indonesia","Taiwan","Japan","Malaysia","Japan","Japan","Japan","China","Taiwan","SouthKorea","Japan","Taiwan","Indonesia","Taiwan","Japan","UnitedStates","Indonesia","Japan","UnitedStates","SouthKorea","Taiwan","Singapore","UnitedStates","UnitedStates","Bangladesh","Japan","UnitedStates","Japan","Taiwan","UnitedStates","Japan","Taiwan","SouthKorea","UnitedStates","Japan","China","Indonesia","Taiwan","UnitedStates","Malaysia","Singapore","Malaysia","Indonesia","Taiwan","Indonesia","UnitedStates","Indonesia","Malaysia","Indonesia","Japan","Malaysia","Indonesia","Japan","Malaysia","Japan","Indonesia","Malaysia","Taiwan","Japan","Japan","Indonesia","Japan","Indonesia","Japan","Australia","Indonesia","Japan","Malaysia","SouthKorea","Japan","Malaysia","Malaysia","Taiwan","Japan","Malaysia","Japan","Malaysia","Singapore","Taiwan","Malaysia","Taiwan","Japan","Malaysia","China","Japan","Malaysia","Singapore","Malaysia","Malaysia","Japan","UnitedStates","Singapore","UnitedStates","China","Japan","Japan","Malaysia","Japan","Taiwan","Japan","Japan","Taiwan","Malaysia","Malaysia","Japan","Malaysia","Japan","China","Japan","SouthKorea","UnitedStates","China","Japan","Hong","Kong","UnitedStates","China","Japan","UnitedStates","Japan","Japan","Japan","UnitedStates","Japan","Japan","UnitedStates","Japan","UnitedStates","Japan","UnitedStates","Indonesia","UnitedStates","Japan","Japan","UnitedStates","Japan","Malaysia","UnitedStates","UnitedStates","UnitedStates","Indonesia","Phillippines","Bangladesh","Brazil","Japan","Brazil","UnitedStates","Japan","Pakistan","Japan","Vietnam","Brazil","Japan","UnitedStates","Indonesia","Japan","Japan","Japan","Japan","Japan","SouthKorea","Taiwan","Taiwan","UnitedStates","UnitedStates","Vietnam","UnitedStates","Phillippines","SouthKorea","Singapore","Brazil","Vietnam","Singapore","Brazil","Bangladesh","UnitedStates","SouthKorea","UnitedStates","Japan","UnitedStates","UnitedStates","Japan","UnitedStates","Japan","UnitedStates","UnitedStates","UnitedStates","Japan","Japan","UnitedStates","Japan","SouthKorea","UnitedStates","UnitedStates","UnitedStates","UnitedStates","Singapore","UnitedStates","UnitedStates","UnitedStates"]
Style = ["Pack","Pack","Pack","Pack","Pack","Pack","Cup","Pack","Box","Bowl","Pack","Bowl","Tray","Bowl","Cup","Pack","Pack","Box","Pack","Pack","Box","Bowl","Bowl","Pack","Tray","Pack","Bowl","Box","Cup","Bowl","Bowl","Pack","Bowl","Box","Boowl","Bowl","Bowl","Box","Bowl","Bowl","Pack","Cup","Pack","Pack","Pack","Bowl"]
Brand = ["Jasmine","Indomie","MAMA","Ottogi","Samyang","Foods","Jasmine","Sapporo","Ichiban","Best","Wok","NoodleMix","Sugakiya","Daebak","Nissin","Nissin","Acecook","Fan's","Mom's","Dry","Noodle","The","Han","Kitchen","Ippudo","A-Sha","Kobe","NoodleMix","Acecook","Nongshim","Best","Wok","Daikoku","Samyang","Foods","Samyang","Foods","NoodleMix","Nissin","Tapatio","Cielo","Pran","Maruchan","VIZ","Nissin","NoodleMix","Cielo","Ippudo","NoodleMix","Samyang","Foods","Thai","Kitchen","Acecook","Jinmailiang","Indomie","A-Sha","Thai","Authentic"]
filteredlist = []
#Init





#Fun
def randomtype():
    q = input("Would you like to have a random ramen? (Y/N)")
    qp = q.lower()
    if qp == "y":
        for i in range(1):
          filteredlist.append(ramentypes[i])
          print("I recommend the " + (random.choice(filteredlist)) )
    else:
       print("uh oh you didnt press y")

def country3():
   try:
      print("""
   Malaysia,
   Indonesia,
   Thailand,
   UnitedStates,
   Taiwan,
   Japan,
   China,
   SouthKorea,
   Phillippines,5
   Bangladesh,
   """)

      w = input("What country would you like to get your ramen from?")

      y = country.index(w)

      print("One of the ramen from " + str(w) + " is  The " + str(Brand[
   y]) + " " + str(ramentypes[y]) + "it comes in a " + str(Style[y]))
   except:
      print("Invalid Response Try again")


def ramendep():
   try:
      x = input("What specific ramen would you like?")
      p = ramentypes.index(x)
      print(str(x) + " rating is " + str(ratings[p]) + " out of 5"  )

   except:
      print("Uh oh your response was invalid")


def menu(option):
   if option == "y":
      print("welcome to the Ramen Picker!")
      while True:
       print("What would you like to do?")
       h = int(input("""1:look at a random ramen type,"
       2:Select a country that a ramen is from?"
       3:Find a specific ramen that is in the list and say its rating
       4:Quit"""))

       if h == 1:
         randomtype()

       if h == 2:
          country3()

       if h == 3:
          ramendep()

       if h == 4:
          print("Goodbye!")
          break











menu(input("would you like to go the the ramen stuf? (y/n)"))






# The ramen information was taken from https://www.theramenrater.com/resources-2/the-list/ under a Creative Commons License (CC BY-NC-SA 4.0).



