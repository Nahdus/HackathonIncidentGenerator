import random

P1_rootCause = ["Total power failure at the tower. Immediate restoration required to resume services.", "Severe storm damage has knocked out the tower. Immediate assessment and repairs are necessary.", "Major hardware failure detected. All communication services are offline. Urgent replacement needed.", "Battery low node running on power saver mode", "Core network component failure affecting the entire tower. Critical to restore connectivity urgently.", " Fiber optic cable cut has resulted in a complete service outage. Immediate repair teams needed."]

P2_rootCause = ["Cooling system failure detected, putting equipment at risk of overheating. Immediate repair necessary."]

P3_rootCause = ["High traffic leading to network congestion. Evaluate capacity and consider load balancing solutions."]



p1_description = ["Total power failure at the tower. Immediate restoration required to resume services.", "Severe storm damage has knocked out the tower. Immediate assessment and repairs are necessary.", "Major hardware failure detected. All communication services are offline. Urgent replacement needed.", "Battery low node running on power saver mode", "Core network component failure affecting the entire tower. Critical to restore connectivity urgently.", " Fiber optic cable cut has resulted in a complete service outage. Immediate repair teams needed.",
                  "Unauthorized access detected at the tower site, leading to system shutdown for safety. Security response required.","Fire alarm activated, leading to automatic shutdown of services. Emergency response team required on-site.",
                  "System crash detected, causing total service disruption. Immediate reboot and troubleshooting required.","Vandalism reported at the tower site, resulting in equipment damage and service loss. Urgent repair and investigation needed.",
                  "Toxic spill near the tower site has led to evacuation and service shutdown. Immediate hazard assessment and cleanup required."]
p2_description = ["Users report intermittent signal loss and dropped calls. Investigation required to identify the source of the problem.",
                  "Customers experiencing slow data speeds affecting streaming and browsing. Urgent diagnostics needed.",
                  "Backup generator is malfunctioning, risking downtime in case of a power failure. Immediate repair is necessary.",
                  "Current hardware nearing capacity limits. Recommend upgrade to prevent potential service degradation.",
                  "Significant uptick in customer complaints about call quality. Urgent review of node performance required.",
                  "Configuration error detected in router settings, affecting connectivity. Immediate resolution needed to restore normal service.",
                  "LAN issues reported, causing delays in data transmission. Urgent investigation required.",
                  "Cooling system failure detected, putting equipment at risk of overheating. Immediate repair necessary.",
                  "High traffic leading to network congestion. Evaluate capacity and consider load balancing solutions.",
                  "Critical software updates pending that could improve performance and security. Schedule urgent implementation."]
p3_description = ["Scheduled maintenance service interruptions expected. Notify customers in advance.",
                  "Firmware update scheduled for next week to improve performance. No immediate impact, but recommend monitoring.",
                  "Uninterruptible Power Supply (UPS) showing low battery alert. Replacement scheduled, but monitoring is advised.",
                  "Equipment calibration recommended to ensure optimal performance. Schedule",
                  "User feedback indicates slight concerns with call clarity. Monitor performance for any necessary adjustments.",
                  "Review of network optimization strategies pending. No immediate impact, but should be addressed soon.",
                  "Inventory check for spare parts and equipment required to ensure readiness for future issues. Schedule within the next two weeks.",
                  "Alert for low signal strength detected in specific areas. Recommend monitoring and further analysis.",
                  "Regular cable maintenance needed to prevent future issues. Scheduled",
                  "Documentation for tower operations is outdated. Update required to reflect current configurations and procedures."]
p4_description = ["Prepare and review the monthly performance report for Node 1B. No immediate impact on operations.",
                  "Review and update documentation for maintenance procedures. Schedule at your convenience.",
                  "Conduct a minor inspection of equipment to ensure everything is in working order. No urgent issues reported.",
                  "Analyze user survey results for feedback on service quality. Schedule for the end of the month.",
                  "Label cables for better organization in the equipment room. Can be completed at a later date.",
                  "Reminder to conduct an inventory audit in the next quarter. No immediate action required.",
                  "Schedule a training session for new staff on equipment operation. Date to be determined.",
                  "New software version available; however, it is not critical to update immediately. Monitor for improvements.",
                  "Develop a plan for community engagement activities. No immediate deadlines.",
                  "Organize a facility clean-up for the equipment room. Schedule when convenient."]

pulse_tickets_description = [
    "User reports occasional call disconnections during conversations. Not widespread, but needs monitoring.",
    "User experiencing low bandwidth during peak hours. Not affecting all users; recommend monitoring.",
    "Weak password detected in network sys admin systems"
    "User reports weak signal strength in their location. No widespread outage, but check for possible interference.",
    "User reports slow internet speeds, especially during evening hours. Monitor network usage for potential congestion.",
    "User experiencing frequent internet disconnections. Check connection stability but not affecting the entire network.",
    "User reports buffering issues while streaming video content. Recommend checking for local congestion.",
    "Misconfigured Firewalls detected in network Sysadmin Panels"
    "User reports dropped calls specifically near their home. Investigate local coverage, but not widespread.",
    "Unsecured APIs found exposed to vulnerability"
    "User reports high latency while gaming. Isolated incident; monitor for broader issues.",
    "User experiencing poor quality during VoIP calls. Check network stability, but not affecting all users.",
    "User reports delays in email delivery. Investigate potential local server issues, but not affecting all users."
    "unpatched software is still being used in admin panel"
]


def chooseRandom(listOfChoice):
    return random.choice(listOfChoice)

def createTicket(nodeId,priority):
    match priority:
        case "p1":
            description = chooseRandom(p1_description)
            return {
            "priority":"p1",
            "nodeid":nodeId,
            "heading":description[0:10],
            "description":description,
            }
            
        case "p2":
            description = chooseRandom(p1_description)
            return {
            "priority":"p2",
            "nodeid":nodeId,
            "heading":description[0:10],
            "description":description
            }
        case "p3":
            description = chooseRandom(p1_description)
            return {
            "priority":"p3",
            "nodeid":nodeId,
            "heading":description[0:10],
            "description":description
            }
        case "p4":
            description = chooseRandom(p1_description)
            return {
            "priority":"p4",
            "nodeid":nodeId,
            "heading":description[0:10],
            "description":description
            }
        case "p5":
            description = chooseRandom(p1_description)
            return {
            "priority":"p5",
            "nodeid":nodeId,
            "heading":description[0:10],
            "description":description
            }