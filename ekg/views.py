# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from ekg.models import EKG
from pulse.models import Pulse
from pulse.generator import generate_pulses
from random import choice


def ekg(request, ekg_id, outputtype):
    ekg = get_object_or_404(EKG, id=ekg_id)
    if ekg.pulse_generated == False:
        generate_pulses(ekg)
        ekg.pulse_generated = True
        ekg.save()

    pulses = Pulse.objects.filter(ekg=ekg).order_by("id")
    if outputtype == 'json':
        return render_to_response('ekg.json', {"ekg": ekg, "pulses":pulses},
                                  mimetype='application/json')
    return render_to_response('ekg.html', {"ekg": ekg, "pulses":pulses})


def instant(request, ekg_id, outputtype):
    if int(ekg_id) == 0:
        ekg = choice(EKG.objects.all())
        rastgele = True
    else:
        ekg = get_object_or_404(EKG, id=ekg_id)
        rastgele = False

    if ekg.pulse_generated == False:
        generate_pulses(ekg)
        ekg.pulse_generated = True
        ekg.save()

    available_pulses = Pulse.objects.filter(ekg=ekg).order_by("id")
    number_of_pulses = len(available_pulses)

    if ekg.last_sent == (number_of_pulses-1):
        current = 1
    else:
        current = ekg.last_sent + 1

    pulse = available_pulses[current]
    ekg.last_sent = current
    ekg.save()

    if outputtype == 'json':
        return render_to_response('instant.json',
                                  {"pulse": pulse, "rastgele": rastgele},
                                  mimetype='application/json')
    return render_to_response('instant.html',
                              {"pulse": pulse, "rastgele": rastgele})
