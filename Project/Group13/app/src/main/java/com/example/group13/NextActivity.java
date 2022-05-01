package com.example.group13;

import androidx.annotation.Nullable;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.TextView;
import android.widget.ListView;

public class  NextActivity extends Activity {

    ListView listView;
    String[] items;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_next);
        Intent startedIntent = getIntent();
        String songlist = (String) startedIntent.getCharSequenceExtra("songlist");
        items = songlist.split("\n");
        for (String song : items) {
            Log.d("SONGS", song);
        }
        Log.d("SONGS", "test");
        listView = (ListView)findViewById(R.id.listViewSong);
        displaySongs();
    }
    void displaySongs() {
        customAdapter customAdapter = new customAdapter();
        listView.setAdapter(customAdapter);
    }

    class customAdapter extends BaseAdapter
    {

        @Override
        public int getCount() {
            return items.length;
        }

        @Override
        public Object getItem(int i) {
            return null;
        }

        @Override
        public long getItemId(int i) {
            return 0;
        }

        @Override
        public View getView(int i, View view, ViewGroup viewGroup) {
            //Might be an issue
            View myView = getLayoutInflater().inflate(R.layout.activity_next, null);
            TextView textsong = myView.findViewById(R.id.txtsongname);
            textsong.setSelected(true);
            textsong.setText("test");

            return myView;
        }
    }
}