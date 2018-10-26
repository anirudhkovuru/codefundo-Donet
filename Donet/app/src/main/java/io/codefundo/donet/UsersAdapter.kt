package io.codefundo.donet

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import java.util.*



class UsersAdapter(private var items: ArrayList<UserDto>): RecyclerView.Adapter<UsersAdapter.ViewHolder>() {
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        var userDto = items[position]
        holder?.txtName?.text = userDto.name
        holder?.txtComment?.text = userDto.comment    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val itemView = LayoutInflater.from(parent?.context)
                .inflate(R.layout.user_list_row, parent, false)

        return ViewHolder(itemView)    }

    override fun getItemCount(): Int {
        return items.size
    }


    class ViewHolder(row: View) : RecyclerView.ViewHolder(row) {
        var txtName: TextView? = null
        var txtComment: TextView? = null

        init {
            this.txtName = row?.findViewById<TextView>(R.id.txtName)
            this.txtComment = row?.findViewById<TextView>(R.id.txtComment)
        }
    }
}