package com.example.myapp;

import android.util.Log;
import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

public class MyFirebaseMessagingService extends FirebaseMessagingService {
    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        Log.d("FCM", "Message received: " + remoteMessage.getData());
        // TODO: build and show a notification based on payload
    }

    @Override
    public void onNewToken(String token) {
        Log.d("FCM", "New token: " + token);
        // TODO: send token to your backend if needed
    }
}
