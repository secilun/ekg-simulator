from pulse.models import Pulse


def generate_pulses(EKG_object):
    pulses1 = EKG_object.pulse1.split(",")
    ptypes1 = EKG_object.ptype1.split(",")

    pulses2 = EKG_object.pulse2.split(",")
    ptypes2 = EKG_object.ptype2.split(",")

    pulses3 = EKG_object.pulse3.split(",")
    ptypes3 = EKG_object.ptype3.split(",")

    for i in range(len(pulses1)):
        Pulse.objects.create(
            ekg=EKG_object,
            pulse1=pulses1[i], ptype1=ptypes1[i],
            pulse2=pulses2[i], ptype2=ptypes2[i],
            pulse3=pulses3[i], ptype3=ptypes3[i],
        )

