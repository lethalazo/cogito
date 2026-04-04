"use client"

import { useRef } from "react"
import { motion, useScroll, useTransform } from "framer-motion"
import { SectionWrapper } from "@/components/shared/section-wrapper"
import { SectionHeading } from "@/components/shared/section-heading"
import { PullQuote } from "@/components/shared/pull-quote"
import { SectionParticles } from "@/components/canvas/section-particles"

export function ProblemSection() {
  const sectionRef = useRef<HTMLDivElement>(null)
  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start end", "end start"],
  })
  const lineHeight = useTransform(scrollYProgress, [0.1, 0.5], ["0%", "100%"])

  return (
    <SectionWrapper id="problem">
      <SectionParticles mode="drift" count={20} maxOpacity={0.12} />
      <SectionHeading number="01" title="THE PROBLEM" />

      <div ref={sectionRef} className="max-w-[720px] mx-auto relative px-2 sm:px-0">
        <motion.div
          className="absolute -left-8 top-0 w-px bg-accent/20 hidden lg:block"
          style={{ height: lineHeight }}
        />

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-60px" }}
          transition={{ duration: 0.7 }}
          className="font-serif text-2xl sm:text-3xl md:text-4xl text-foreground mb-8"
        >
          AI forgot how to remember.
        </motion.p>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-60px" }}
          transition={{ duration: 0.7, delay: 0.1 }}
          className="prose-body mb-8"
        >
          Every major AI platform works the same way: you type, it responds, the
          conversation ends, and everything vanishes. The next time you return,
          you start from zero. The AI doesn&apos;t know who you are, what you
          care about, or what you discussed yesterday.
        </motion.p>

        <PullQuote>
          Every conversation starts from zero. Your context is their product.
        </PullQuote>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-60px" }}
          transition={{ duration: 0.7, delay: 0.2 }}
          className="prose-body mb-8"
        >
          The platforms that do retain your data do so on their terms —
          centralized, unencrypted, used for training. You&apos;re locked into
          one provider. Your conversations feed the machine. You have no
          portability, no privacy, and no ownership.
        </motion.p>

        <motion.p
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-60px" }}
          transition={{ duration: 0.7, delay: 0.3 }}
          className="prose-body"
        >
          The intelligence is commoditized. What&apos;s missing is{" "}
          <span className="text-accent font-medium">cognition</span> — the
          ability to remember, learn, and build understanding over time. That
          requires a fundamentally different architecture.
        </motion.p>
      </div>
    </SectionWrapper>
  )
}
