package io.codefundo.donet

import android.os.Bundle

import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.DefaultItemAnimator
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class ToDonate: AppCompatActivity() {

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

        var user: UserDto = UserDto("DWF", "Balance is: " + 1)
        result.add(user)
        var user2: UserDto = UserDto("ASE", "Balance is: " + 14)
        result.add(user2)
        var user3: UserDto = UserDto("REW", "Balance is: " + 8)
        result.add(user3)
        var user4: UserDto = UserDto("AWQ", "Balance is: " + 4)
        result.add(user4)
        var user5: UserDto = UserDto("PFR", "Balance is: " + 9)
        result.add(user5)




        return result
    }

}
