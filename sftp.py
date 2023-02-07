from smtplib import SMTP
import paramiko
import smtplib

def enviar_arquivos_via_sftp():
    try:
        paramiko.util.log_to_file("paramiko.log")

        host, port = "endereço.daadp.adp.com", 10025
        transport = paramiko.Transport((host, port))

        username, password = "usuario", "senha"
        transport.connect(None, username, password)

        sftp = paramiko.SFTPClient.from_transport(transport)

        sftp.put('C:/caminho', '/nomedoarquivo1.txt')
        sftp.put('C:/caminho', '/nomedoarquivo2.txt')
        sftp.put('C:/caminho', '/nomedoarquivo3.txt')

        sftp.close()
        transport.close()

    except:
        subject = "Erro ao enviar arquivos para ADP"
        message = "\nHouve um erro ao enviar os arquivos para ADP"
        msg = "Subject: {}\n\n{}".format(subject, message)
        mailserver: SMTP = smtplib.SMTP('smtp.com.br', 587)
        mailserver.ehlo()
        mailserver.starttls()

        emailsenviar = ['seuemail@coisa.com.br']
        mailserver.login('emailsaida@coisa.com.br', 'senhaemail')
        mailserver.sendmail('emailsaida@coisa.com.br', emailsenviar, msg, mail_options=())
        mailserver.quit()


enviar_arquivos_via_sftp()
