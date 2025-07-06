import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message

class ChatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_message = request.data.get('message')
        username = request.user.username

        # Sauvegarde dans MongoDB
        Message(sender=username, content=user_message, role="user").save()

        # Appel API Groq
        groq_key = 'YOUR_GROQ_API_KEY'  # Remplacez par votre clé API Groq
        url = 'https://api.groq.com/openai/v1/chat/completions'

        headers = {
            'Authorization': f'Bearer {groq_key}',
            'Content-Type': 'application/json'
        }

        payload = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": user_message}],
            "temperature": 0.7
        }

        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        # Debug : afficher la réponse complète dans les logs pour comprendre d’éventuelles erreurs
        print("Réponse API Groq:", data)

        if "choices" not in data:
            # Retourner une erreur claire avec détails pour debugging
            return Response({
                "error": "Réponse inattendue de l'API Groq, pas de clé 'choices'.",
                "details": data
            }, status=500)

        bot_reply = data["choices"][0]["message"]["content"]

        # Sauvegarde réponse bot
        Message(sender="bot", content=bot_reply, role="assistant").save()

        return Response({"response": bot_reply})



class ChatHistoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        username = request.user.username
        # Récupérer tous les messages de cet utilisateur ET du bot (conversation complète)
        messages = Message.objects.filter(sender__in=[username, "bot"]).order_by('timestamp')
        
        # Formater la réponse en liste simple
        history = []
        for msg in messages:
            history.append({
                "sender": msg.sender,
                "content": msg.content,
                "role": msg.role,
                "timestamp": msg.timestamp.isoformat()
            })

        return Response(history)
