from pulse.models import Pulse


def generate_pulses(EKG_object):
    pulses = EKG_object.pulse.split(",")
    for pulse in pulses:
        Pulse.objects.create(ekg=EKG_object, pulse=pulse)
