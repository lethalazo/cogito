"use client"

import { useRef } from "react"
import { motion, useScroll, useTransform } from "framer-motion"
import { useTypingEffect } from "@/hooks/use-typing-effect"
import { HeroNetwork } from "@/components/canvas/hero-network"

export function Opening() {
  const { displayedText, isComplete } = useTypingEffect({
    text: "The AI that remembers. Your data stays yours.",
    speed: 35,
    startDelay: 1200,
  })

  const sectionRef = useRef<HTMLDivElement>(null)
  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start start", "end start"],
  })
  const contentOpacity = useTransform(scrollYProgress, [0, 0.5], [1, 0])
  const contentY = useTransform(scrollYProgress, [0, 0.5], [0, -60])

  return (
    <section
      ref={sectionRef}
      className="relative min-h-screen flex items-center justify-center overflow-hidden bg-background"
    >
      {/* Canvas particle network */}
      <div className="absolute inset-0 z-0">
        <HeroNetwork />
      </div>

      {/* Subtle center glow */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_rgba(212,99,94,0.04)_0%,_transparent_50%)] z-[1]" />

      {/* Edge vignette — fade to cream */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_transparent_25%,_rgba(250,247,242,0.75)_100%)] z-[1]" />

      {/* Content */}
      <motion.div
        className="relative z-10 text-center px-6 max-w-5xl"
        style={{ opacity: contentOpacity, y: contentY }}
      >
        <motion.div
          initial={{ scaleX: 0 }}
          animate={{ scaleX: 1 }}
          transition={{ duration: 1.2, delay: 0.3, ease: "easeOut" }}
          className="w-12 h-px bg-accent/40 mx-auto mb-10 origin-center"
        />

        <motion.h1
          initial={{ opacity: 0, y: 25 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, delay: 0.3, ease: "easeOut" }}
          className="font-serif text-[10vw] sm:text-5xl md:text-7xl lg:text-[5.5rem] tracking-[0.02em] sm:tracking-[0.08em] md:tracking-[0.12em] text-foreground mb-3 whitespace-nowrap"
        >
          COGITO
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.7, ease: "easeOut" }}
          className="font-mono text-[10px] sm:text-xs tracking-[0.2em] sm:tracking-[0.3em] uppercase text-accent mb-16 sm:mb-20"
        >
          COGNITIVE AI
        </motion.p>

        <motion.div
          initial={{ scaleX: 0 }}
          animate={{ scaleX: 1 }}
          transition={{ duration: 0.8, delay: 1 }}
          className="w-20 h-px bg-gradient-to-r from-transparent via-accent/50 to-transparent mx-auto mb-12 origin-center"
        />

        <div className="min-h-[5rem] md:min-h-[4rem]">
          <p className="text-base sm:text-xl md:text-2xl text-foreground/50 leading-relaxed max-w-3xl mx-auto font-serif italic px-2">
            {displayedText}
            {!isComplete && (
              <span className="animate-blink text-accent ml-0.5">|</span>
            )}
          </p>
        </div>
      </motion.div>

      {/* Scroll indicator */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 4, duration: 1 }}
        className="absolute bottom-8 left-1/2 -translate-x-1/2 z-10 flex flex-col items-center gap-2"
      >
        <span className="font-mono text-[10px] tracking-[0.3em] uppercase text-accent/25">
          Scroll
        </span>
        <motion.span
          animate={{ y: [0, 8, 0] }}
          transition={{ duration: 2.5, repeat: Infinity, ease: "easeInOut" }}
          className="block text-accent/30 text-lg"
        >
          ↓
        </motion.span>
      </motion.div>
    </section>
  )
}
