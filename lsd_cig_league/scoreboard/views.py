from django.shortcuts import render, redirect
from .models import Participant, Event, Score

def scoreboard_view(request):
    events = Event.objects.all()
    participants = Participant.objects.all()

    # Create a dictionary to hold scores for each event
    scoreboard = []
    participant_totals = {participant.name: 0 for participant in participants}

    for event in events:
        row = {'event': event.name}
        for participant in participants:
            score = Score.objects.filter(event=event, participant=participant).first()
            score_value = score.score if score else 0
            row[participant.name] = score_value
            participant_totals[participant.name] += score_value
        scoreboard.append(row)

    context = {
        'scoreboard': scoreboard,
        'participants': participants,
        'participant_totals': participant_totals,
    }
    return render(request, 'scoreboard/scoreboard.html', context)

# def admin_view(request):
#     return redirect(request, "/admin")