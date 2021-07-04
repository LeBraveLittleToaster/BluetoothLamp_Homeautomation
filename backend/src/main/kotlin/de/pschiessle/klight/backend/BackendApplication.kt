package de.pschiessle.klight.backend

import ReactiveWebSocketHandler
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.Bean
import org.springframework.core.Ordered
import org.springframework.web.cors.CorsConfiguration
import org.springframework.web.cors.CorsConfigurationSource
import org.springframework.web.cors.UrlBasedCorsConfigurationSource
import org.springframework.web.reactive.HandlerMapping
import org.springframework.web.reactive.handler.SimpleUrlHandlerMapping
import org.springframework.web.reactive.socket.WebSocketHandler
import org.springframework.web.reactive.socket.server.WebSocketService
import org.springframework.web.reactive.socket.server.support.HandshakeWebSocketService
import org.springframework.web.reactive.socket.server.support.WebSocketHandlerAdapter
import org.springframework.web.reactive.socket.server.upgrade.ReactorNettyRequestUpgradeStrategy
import java.util.*


@SpringBootApplication
class BackendApplication() {

    @Bean
    fun getWsController(): ReactiveWebSocketHandler {
        return ReactiveWebSocketHandler()
    }

    @Bean
    fun handlerMapping(): HandlerMapping {
        println("Creating mapping...")
        val map: MutableMap<String, WebSocketHandler> = HashMap()
        map["/echo"] = getWsController()
        val mapping = SimpleUrlHandlerMapping()
        mapping.urlMap = map
        mapping.order = Ordered.HIGHEST_PRECEDENCE
        return mapping
    }

    @Bean
    fun handlerAdapter(): WebSocketHandlerAdapter? {
        return WebSocketHandlerAdapter(webSocketService()!!)
    }

    @Bean
    fun webSocketService(): WebSocketService? {
        return HandshakeWebSocketService(ReactorNettyRequestUpgradeStrategy())
    }
}

fun main(args: Array<String>) {
    runApplication<BackendApplication>(*args)
}
