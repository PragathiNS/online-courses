### Reusing the same xml file for multiple activities
Removing the tools:context from the root tag makes an xml file be accessed by multiple activities

For Example,  
word_list.xml  
`<ListView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/list"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:paddingBottom="@dimen/activity_vertical_margin"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"`
    ~~tools:context="com.example.appName.WordsActivity"~~`/>`
    
In WordsActivity and NamesActivity, the onCreate method will have the setContentView as follows,
`setContentView(R.layout.word_list);`
