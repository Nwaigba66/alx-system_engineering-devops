#Postmortem

Postmortem for gloriaconsult.com.ng

##Issue Summary:

This incidence report gives a breakdown of the outage that occurred from the period of 10th of October to 15th of October 2023 on the domain website of gloriaconsult.com.ng that affected 100% of customers. This outage was a result of a wordpress website with file name /radio hosted on the domain gloriaconsult.com.ng/radio (A website for radio frequencies communication in Africa). The website was completely removed from the server side of the hosting platform.

##Name of Issue: 
- DNS-error /issue with website
- Error “This site can’t be reached”
DNS_PROBE_FINISHED_NXDOMAIN


##Timeline:
- 10/10/23: Around 7:00 WAT, the website was completely down with the error message “site can’t be reached”
- 10/10/23: The Engineer reported she got an error Error “This site can’t be reached”
DNS_PROBE_FINISHED_NXDOMAIN
- 10/10/23: Engineer on duty contacted the hosting platform to identify the root cause of the error.
- 11/10/23: The hosting platform responded that the domain renewal expired due to late renewal the domain was removed from their server with no available back-up
- 12/10/23: The renewal was paid and the host website was recreated
- 13/10/23: Engineer tried to access the website again but a second error message appeared.
Error “NOT found, the requested URL was not found on this server. Additionally a 404 not found error was encountered while trying to use an error document to handle the request”

- 14/10/23: Engineer contacted hosting platform again and got a response that the source of the error was discovered to be the lost of the /radio file on the sever.



##Root cause and Resolution:
- Root cause: The root cause of the issue was as a result of loss of files due to inability to renew in due time.
- There was no available backup done from the side of the hosting platform so they had to recreate the host again and told the Engineer to upload the files afresh.
- The company registered email with the hosting platform  is a yahoo mail. The webmail from the domain name can no longer send messages to  any yahoomail addresses. 
- All reminder emails to the company’s yahoomail were not forwarded so the Engineer responsible for renewal were not alerted before the domain expired that affected the wordpress file /radio


##Corrective and Preventive measures:
- The first flaw was that the hosting platform did not send a reminder about the domain renewal or perhaps that was a lack of communication on the domain renewal
- The yahoo mail has been changed to google mail on the side of the hosting company for easy, quick and better communication.
- Domain renewal should be paid in due time before expiration date.
- The files were uploaded again and the wordpress website will be accessible again to users.

