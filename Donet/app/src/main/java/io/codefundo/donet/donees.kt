package io.codefundo.donet

import android.os.Bundle

import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.DefaultItemAnimator
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class donees: AppCompatActivity() {

    private var recyclerView: RecyclerView? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.donee_view)

        recyclerView = findViewById(R.id.recyclerView)
        var adapter = UsersAdapter(generateData())
        val layoutManager = LinearLayoutManager(applicationContext)
        recyclerView?.layoutManager = layoutManager
        recyclerView?.itemAnimator = DefaultItemAnimator() as RecyclerView.ItemAnimator?

        recyclerView?.adapter = adapter
        adapter.notifyDataSetChanged()
    }

    private fun generateData(): ArrayList<UserDto> {
        var result = ArrayList<UserDto>()

            var user: UserDto = UserDto("XYZ", "Balance is: " + 25)
            result.add(user)
        var user2: UserDto = UserDto("ABC", "Balance is: " + 12)
        result.add(user2)
        var user3: UserDto = UserDto("DSA", "Balance is: " + 0.5)
        result.add(user3)
        var user4: UserDto = UserDto("IRE", "Balance is: " + 42)
        result.add(user4)
        var user5: UserDto = UserDto("ACN", "Balance is: " + 20)
        result.add(user5)




        return result
    }

}
