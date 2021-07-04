package de.pschiessle.klight.backend.data

import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.ComponentScan
import org.springframework.context.annotation.Configuration
import org.springframework.web.socket.CloseStatus
import org.springframework.web.socket.TextMessage
import org.springframework.web.socket.WebSocketSession
import org.springframework.web.socket.config.annotation.EnableWebSocket
import org.springframework.web.socket.config.annotation.WebSocketConfigurer
import org.springframework.web.socket.config.annotation.WebSocketHandlerRegistry
import org.springframework.web.socket.handler.TextWebSocketHandler
import java.util.concurrent.atomic.AtomicLong
import java.util.logging.LogManager


data class User(val id: Long, val name: String)
data class Message(val msgType: String, val data: Any)

class WebSocketerino : TextWebSocketHandler () {
    val sessionList = HashMap<WebSocketSession, User>()
    var uids = AtomicLong(0)

    override fun afterConnectionEstablished(session: WebSocketSession) {
        print("New connecting established")
        super.afterConnectionEstablished(session)
    }

    @Throws(Exception::class)
    override fun afterConnectionClosed(session: WebSocketSession, status: CloseStatus) {
        sessionList -= session
    }

    fun emit (session: WebSocketSession, msg: Message) = session.sendMessage((TextMessage(jacksonObjectMapper().writeValueAsString(msg))))
    fun broadcast(msg:Message) = sessionList.forEach{emit(it.key, msg)}
    fun broadcastToOthers(me: WebSocketSession, msg: Message) = sessionList.filterNot { it.key == me }.forEach{emit(it.key, msg)}

    override fun handleTextMessage(session: WebSocketSession, message: TextMessage) {
        print("Logging test")
        val json = ObjectMapper().readTree(message.payload)
        when(json.get("type").asText()){
            "join" -> {
                val user = User(uids.getAndIncrement(), json.get("data").asText())
                sessionList.put(session, user)
                emit(session, Message("users", sessionList.values))
                broadcastToOthers(session, Message("join", user))
            }
            "say" -> {
                broadcast(Message("say", json.get("data").asText()))
            }
        }
    }
}

@Configuration
@EnableWebSocket
class WsConfig : WebSocketConfigurer {
    override fun registerWebSocketHandlers(registry: WebSocketHandlerRegistry) {
        registry.addHandler(WebSocketerino(), "/chat")
    }
}